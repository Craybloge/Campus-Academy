package fr.campusacademy.oopcourse.tetris.game.mathieuBeta;

import org.newdawn.slick.Color;

public class Block {
	protected Color color;
	
	public Block(Color color) {
	 this.color = color;
	}

	@Override
	public String toString() {
		return  "D";
	}


}
