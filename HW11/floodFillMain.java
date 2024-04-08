import java.util.LinkedList;
import java.util.Queue;

public class floodFillMain {
	 public int[][] floodFill(int[][] image, int sr, int sc, int color) {
		  if(image [sr][sc]== color) {
			  return image;
		  }
		 
		  Queue <int []> q = new LinkedList<>();
		  q.offer(new int [] {sr, sc});
		  int oc = image [sr][sc];
		  image [sr][sc] = color;
		  int [][] directions = {{0,-1}, {0,1}, {-1, 0}, {1, 0}};
		  while(!q.isEmpty()) {
			 int []currentNode = q.poll();
			 int currentRow = currentNode[0];
			 int currentCol = currentNode[1];
			 
			 for( int[] direction: directions) {
				 int x = currentRow + direction[0]; 
				 int y = currentCol + direction[1];
				 if(x >= 0 && x < image.length && y >= 0 && y < image[0].length && image [x][y] == oc) {
					 q.add(new int []{x, y});
					 image [x][y] = color;
				 }
			 }
			 
		  }
		  return image;
	 }
      public static void main (String [] args) {
    	  
    	  floodFillMain image1 = new floodFillMain();
    	  int image [][] = {{1,1,1}, {1,1,0}, {1,0,1}};

    	  image1.floodFill(image, 1, 1, 2); 
    	  for(int i = 0; i < image.length; i++) {
    		  for( int j = 0; j < image.length; j++) {
    		  System.out.print(image[i][j] + " ");
    	  }
    		  System.out.println();
    	  } 
      }
}
