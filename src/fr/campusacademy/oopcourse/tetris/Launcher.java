package fr.campusacademy.oopcourse.tetris;
import static org.lwjgl.glfw.GLFW.*;

import org.lwjgl.glfw.GLFWVidMode;
public class Launcher {
	public static void main(String[] args) {
		if (!glfwInit()) {
			throw new IllegalStateException("Failed to initialize GLFW!");
		}
		
		glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
		long window = glfwCreateWindow(640, 480, "tetris", 0, 0);
		
		if (window == 0) {
			throw new IllegalStateException("Failed to create window!");
		}
		
		GLFWVidMode videomode = glfwGetVideoMode(glfwGetPrimaryMonitor());
		glfwSetWindowPos(window, (videomode.width() - 640) / 2, (videomode.height() - 480) / 2);
		
		glfwShowWindow(window);
	}
}
