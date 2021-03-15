package fr.campusacademy.oopcourse.tetris.game.mathieuBeta;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.newdawn.slick.AppGameContainer;
import org.newdawn.slick.BasicGame;
import org.newdawn.slick.Color;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.SlickException;

public class MathieuBetaTetris extends BasicGame
{
	
	int position = 0;
	
	public MathieuBetaTetris(String gamename)
	{
		super(gamename);
	}

	@Override
	public void init(GameContainer gc) throws SlickException {}

	@Override
	public void update(GameContainer gc, int i) throws SlickException {
		position++;
	}

	@Override
	public void render(GameContainer gc, Graphics g) throws SlickException
	{
		g.drawString("Howdy!", 100, 0 + position);
		
		g.setColor(new Color(49, 50, 30));
		g.fillRect(10, 10+position, 50, 50);
		
	}

	public static void main(String[] args)
	{
		try
		{
			AppGameContainer appgc;
			appgc = new AppGameContainer(new MathieuBetaTetris("Simple Slick Game"));
			appgc.setDisplayMode(640, 480, false);
			appgc.setTargetFrameRate(1);
			appgc.start();
		}
		catch (SlickException ex)
		{
			Logger.getLogger(MathieuBetaTetris.class.getName()).log(Level.SEVERE, null, ex);
		}
	}
}