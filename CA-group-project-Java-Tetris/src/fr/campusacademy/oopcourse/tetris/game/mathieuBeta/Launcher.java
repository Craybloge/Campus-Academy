package fr.campusacademy.oopcourse.tetris.game.mathieuBeta;

import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.newdawn.slick.AppGameContainer;
import org.newdawn.slick.BasicGame;
import org.newdawn.slick.Color;
import org.newdawn.slick.Game;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Input;
import org.newdawn.slick.SlickException;


public class Launcher extends BasicGame {
	static Block[][] playfield = new Block[20][10];
	Piece currentPiece;
	int posy = 0;
	int x = 0;
	int y = 0;
	int posx = 0;
	int max = 10;
	Color purple = new Color(128, 0, 128);
	boolean alternance = true;
	int i = 0; 
	int rotation = 0;
	String[] pool = new String[0];

	public Launcher(String title) {
		super(title);
	}

	public static void main(String[] args) {
		Input.disableControllers();
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
					playfield[y][x] = playfield[y - 1][x];
				}
			}
			count = 0;

		}
	}

	public static void initializing() {

		try {
			AppGameContainer appgc;
			appgc = new AppGameContainer(new Launcher("Simple Slick Game"));
			appgc.setDisplayMode(500, 1000, false);
			appgc.setTargetFrameRate(20);
			appgc.start();
		} catch (SlickException ex) {
			Logger.getLogger(MathieuBetaTetris.class.getName()).log(Level.SEVERE, null, ex);
		}
	}

	public String[] removePieceFromArray(int index, String[] pool) {
		String[] copy = new String[pool.length - 1];

		for (int k = 0, j = 0; k < pool.length; k++) {
		    if (k != index) {
		        copy[j++] = pool[k];
		    }
		}
		return pool = copy;
	}
	public String[] getNewPool() {
		Random rand=new Random();
		String[] pool = {"t", "s", "l", "i", "o", "j", "z"};
		String[] orderedPool= new String[7];
		for (int i = 0; i < 7; i++) {
			int next = rand.nextInt(7-i);
			orderedPool[i] = pool[next];
			System.out.println(orderedPool[i]);
			
		}
		return orderedPool;
	}
	public Piece createNewPiece() {
		posx = 3;
		if (pool.length == 0) {
			pool = getNewPool();
		}
		return new Piece(pool[0], posx,posy);

		

	}

	public void setPiece() {
		for (int i = 0; i < 4; i++) {
			playfield[currentPiece.getPiecePosY(i)][currentPiece.getPiecePosX(i)] = new Block(
																							currentPiece.getColor(),
																							currentPiece.getOneCoordX(i),
																							currentPiece.getOneCoordY(i)
																							);
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

	public void pieceMovement(Block[][] playfield) {
		i++;
		if (i == 10) {

			boolean endOfFall = false;
			if (posy == 0) {
				currentPiece = createNewPiece();
				pool = removePieceFromArray(0, pool);
				setPiece();
			}
			for (int i = 0; i < 4; i++) {
				if (currentPiece.getPosy() < playfield.length - currentPiece.getOneCoordY(i)) {
					if (playfield[currentPiece.getPiecePosY(i)+1][currentPiece.getPiecePosX(i)] != null) {
						System.out.println("ok");
						endOfFall = true;

					}
				} else {
					endOfFall = true;
				}
			}
			for (int i = 0; i < 4; i++) {
				if (currentPiece.getPosy() != 0) {
					playfield[currentPiece.getPiecePosY(i)][currentPiece.getPiecePosX(i)] = null;
				}
			}
			posy++;
			currentPiece.setPosy(posy);
			setPiece();
			if (endOfFall) {
				posy = 0;
			}
			i = 0;
		}
	}

	@Override
	public void init(GameContainer arg0) throws SlickException {
		// TODO Auto-generated method stub

	}

	@Override
	public void update(GameContainer arg0, int arg1) throws SlickException {
		pieceMovement(playfield);
		Input input = arg0.getInput();

		
		
		if (input.isKeyDown(Input.KEY_LEFT)) {
			if (currentPiece.getPosy() != 0) {
				for (int i = 0; i < 4; i++) {
					playfield[currentPiece.getPiecePosY(i)][currentPiece.getPiecePosX(i)] = null;
				}
			}
			posx--;
			currentPiece.setPosx(posx);
			setPiece();
		}
		
		
		if (input.isKeyDown(Input.KEY_RIGHT)) {
			if (currentPiece.getPosy() != 0) {
				for (int i = 0; i < 4; i++) {

					playfield[currentPiece.getPiecePosY(i)][currentPiece.getPiecePosX(i)] = null;
				}
			}
			
			posx++;
			currentPiece.setPosx(posx);
			setPiece();
		}
		if (input.isKeyDown(Input.KEY_UP)) {
			if (rotation == 0) {
				rotation = 1;
				currentPiece.setPosx(currentPiece.getPosy());
				currentPiece.setPosy(currentPiece.getPosx());
				setPiece();
			}
			if (rotation == 1) {
				rotation = 2;
				
				
			}
		}
		

		
		
		for (Block[] lines : playfield) {
			for (Block piece : lines) {
				if (piece == null) {
					System.out.print(" ");
				} else {
					System.out.print(piece);
				}
			}
			System.out.println("");
		}
		checkCompleteLine(playfield);
	}

}
