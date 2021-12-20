package fr.campusacademy.oopcourse.tetris.game.mathieuBeta;

import org.newdawn.slick.Color;

public class Block {
	protected Color color;
	protected int posX;
	protected int posY;
	
	public Block(Color color, int x, int y) {
	 this.color = color;
	 this.posX = x;
	 this.posY = y;
	}
	
	public Color getColor() {
		return color;
	}

	public void setColor(Color color) {
		this.color = color;
	}

	public int getPosX() {
		return posX;
	}

	public void setPosX(int posX) {
		this.posX = posX;
	}

	public int getPosY() {
		return posY;
	}

	public void setPosY(int posY) {
		this.posY = posY;
	}


	@Override
	public String toString() {
		return  "D";
	}


}
