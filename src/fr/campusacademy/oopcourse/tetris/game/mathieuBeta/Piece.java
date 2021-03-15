package fr.campusacademy.oopcourse.tetris.game.mathieuBeta;

import org.newdawn.slick.Color;

public class Piece {
	protected Color color;
	protected int[][] coord = new int[4][2];

	public Piece(String name) {
		if (name == "t") {
			this.color = new Color(128, 0, 128);
			this.coord[0][0] = 0;
			this.coord[0][1] = 0;
			this.coord[1][0] = 0;
			this.coord[1][1] = 1;
			this.coord[2][0] = 0;
			this.coord[2][1] = 2;
			this.coord[3][0] = 1;
			this.coord[3][1] = 1;
		}
		if (name == "s") {
			this.color = new Color(0, 255, 0);
			this.coord[0][0] = 0;
			this.coord[0][1] = 1;
			this.coord[1][0] = 0;
			this.coord[1][1] = 2;
			this.coord[2][0] = 1;
			this.coord[2][1] = 0;
			this.coord[3][0] = 1;
			this.coord[3][1] = 1;
		}
		if (name == "l") {
			this.color = new Color(255, 140, 0);
			this.coord[0][0] = 0;
			this.coord[0][1] = 0;
			this.coord[1][0] = 0;
			this.coord[1][1] = 1;
			this.coord[2][0] = 0;
			this.coord[2][1] = 2;
			this.coord[3][0] = 1;
			this.coord[3][1] = 0;
		}
	}
	
	

}
