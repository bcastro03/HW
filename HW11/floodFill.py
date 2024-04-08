from collections import deque


class FloodFillMain:
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        
        queue = deque()
        queue.append((sr, sc))
        oc = image[sr][sc]
        image[sr][sc] = color
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        while queue:
            current_node = queue.popleft()
            current_row, current_col = current_node[0], current_node[1]
            
            for direction in directions:
                x = current_row + direction[0]
                y = current_col + direction[1]
                
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oc:
                    queue.append((x, y))
                    image[x][y] = color
        
        return image

if __name__ == "__main__":
    image1 = FloodFillMain()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    image1.floodFill(image, 1, 1, 2) 
    for i in range(len(image)):
        for j in range(len(image[0])):
            print(image[i][j], end=" ")
        print()