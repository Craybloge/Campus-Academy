package fr.campusacademy.oopcourse.tetris.game.mathieuBeta;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.newdawn.slick.AppGameContainer;
import org.newdawn.slick.BasicGame;
import org.newdawn.slick.Color;
import org.newdawn.slick.Game;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.SlickException;

public class Launcher extends BasicGame{
	static Block [][] playfield = new Block[20][10];
	Piece currentPiece;
	int position = 0;
	int x = 0;
	int y = 0;
	int posx = 0;
	int max = 10;
	Color purple = new Color(128, 0, 128);
	boolean alternance = true;
	
	
	public Launcher(String title) {
		super(title);
	}
	


	public static void main(String[] args) {

		initializing();
		
		
	}
	public void checkCompleteLine(Block[][] playfield) {
		int count = 0;
		
		for (int y = 0; y < playfield.length; y++) {
			for (int x = 0; x < playfield[0].length; x++) {
				if (playfield[y][x] != null) {
					count++;
				}
			}
			if (count == 10) {
				for (int x = 0; x < playfield[0].length; x++) {
					playfield[y][x] = playfield[y-1][x];
				}
			}
			count = 0;
		 
		
		}
	}
	
	public static void initializing() {

		try
		{
			AppGameContainer appgc;
			appgc = new AppGameContainer(new Launcher("Simple Slick Game"));
			appgc.setDisplayMode(500, 1000, false);
			appgc.setTargetFrameRate(2);
			appgc.start();
		}
		catch (SlickException ex)
		{
			Logger.getLogger(MathieuBetaTetris.class.getName()).log(Level.SEVERE, null, ex);
		}
	}

	public Piece createNewPiece() {
		if (alternance) {
			alternance = false;
			return new Piece("s");
		}else {
			alternance = true;
			return new Piece("t");
			
		}
		
	}
	@Override
	public void render(GameContainer arg0, Graphics g) throws SlickException {
		x = 0;
		y = 0;
		for (Block[] line : playfield) {
			for (Block piece : line) {
				if (piece != null) {
					g.setColor(piece.color);
					g.fillRect(x, y, 50, 50);
				}
				x += 50; 
			}
			y += 50;
			x = 0;
		}
		
	}

	@Override
	public void init(GameContainer arg0) throws SlickException {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void update(GameContainer arg0, int arg1) throws SlickException {
		boolean endOfFall = false;
		if(position == 0) {
			currentPiece = createNewPiece();
		}
		position++;
		for (int[] coords : currentPiece.coord) {
			if (position < 19 - coords[0]) {
				if (playfield[position + coords[0] + 1][posx + coords[1]] != null) {
				endOfFall = true;
				}
		}else {
			endOfFall = true;
		}
		}
		if (!endOfFall) {
			for (int[] coords : currentPiece.coord) {
				playfield[position + coords[0] - 1][posx + coords[1]] = null;
			}
		
			for (int[] coords : currentPiece.coord) {
					playfield[position + coords[0]][posx + coords[1]] = new Block(currentPiece.color);
				
			}
		}else {
			position = 0;
		}
		
		
//		if (position<20) {
//			if (playfield[position][posx] == null) {
//				playfield[position][posx] = new Piece();
//				playfield[position-1][posx] = null;
//			}else {
//				playfield[position-1][posx] = new Piece();
//			}
			
//		}

		
		for (Block[] lines : playfield) {
			for (Block piece : lines) {
				if (piece == null) {
					System.out.print(" ");
				}else {
					System.out.print(piece);
				}
			}
			System.out.println("");
		}
		checkCompleteLine(playfield);
	}

	

}
