package fr.campusacademy.oopcourse.tetris.game.mathieuBeta;

import org.newdawn.slick.Color;

public class Piece {
	protected String name;
	protected Color color;
	protected int[][] coord = new int[4][2];
	protected int posx;
	protected int posy;
	

	public Piece(String name, int x, int y) {
		if (name == "t") {
			this.name = "t";
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
			this.name = "s";
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
			this.name = "l";
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
		if (name == "i") {
			this.name = "i";
			this.color = new Color(0, 255, 255);
			this.coord[0][0] = 0;
			this.coord[0][1] = 0;
			this.coord[1][0] = 0;
			this.coord[1][1] = 1;
			this.coord[2][0] = 0;
			this.coord[2][1] = 2;
			this.coord[3][0] = 0;
			this.coord[3][1] = 3;
		}
		if (name == "o") {
			this.name = "o";
			this.color = new Color(255, 255, 0);
			this.coord[0][0] = 0;
			this.coord[0][1] = 0;
			this.coord[1][0] = 0;
			this.coord[1][1] = 1;
			this.coord[2][0] = 1;
			this.coord[2][1] = 0;
			this.coord[3][0] = 1;
			this.coord[3][1] = 1;
		}
		if (name == "j") {
			this.name = "j";
			this.color = new Color(0, 0, 255);
			this.coord[0][0] = 0;
			this.coord[0][1] = 0;
			this.coord[1][0] = 0;
			this.coord[1][1] = 1;
			this.coord[2][0] = 0;
			this.coord[2][1] = 2;
			this.coord[3][0] = 1;
			this.coord[3][1] = 2;
		}
		if (name == "z") {
			this.name = "z";
			this.color = new Color(255, 0, 0);
			this.coord[0][0] = 0;
			this.coord[0][1] = 0;
			this.coord[1][0] = 0;
			this.coord[1][1] = 1;
			this.coord[2][0] = 1;
			this.coord[2][1] = 1;
			this.coord[3][0] = 1;
			this.coord[3][1] = 2;
		}
		this.posx = x;
		this.posy = y;
	
	}
	
	public int getPiecePosY(int i) {
		return coord[i][0]+posy;
	}
	
	public int getPiecePosX(int i) {
		return coord[i][1]+this.posx;
	}
	
	public int getOneCoordY(int i) {
		return coord[i][0];
	}
	
	public int getOneCoordX(int i) {
		return coord[i][1];
	}

	public int getPosx() {
		return posx;
	}

	public void setPosx(int posx) {
		this.posx = posx;
	}

	public int getPosy() {
		return posy;
	}

	public void setPosy(int posy) {
		this.posy = posy;
	}

	public Color getColor() {
		return color;
	}

	public void setColor(Color color) {
		this.color = color;
	}

	public int[][] getCoord() {
		return coord;
	}

	public void setCoord(int[][] coord) {
		this.coord = coord;
	}
	
	

}
