class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols=len(image), len(image[0])
        dirs=[(0,1), (0,-1), (1, 0), (-1, 0)]
        original = image[sr][sc]

        if original == color: 
            return image
        def dfs(image, sr, sc, color):
            if sr<0 or sc<0 or sr>=rows or sc>=cols:
                return
            if image[sr][sc]!=original:
                return
            image[sr][sc]=color
            for dr, dc in dirs:
                dfs(image, sr+dr, sc+dc, color)
        dfs(image, sr,sc, color)
        
        return image
        