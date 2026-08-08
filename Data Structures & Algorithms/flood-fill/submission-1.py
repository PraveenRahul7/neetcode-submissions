class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original=image[sr][sc]
        rows,cols=len(image), len(image[0])
        dirs=[(0,1), (0,-1), (1,0), (-1,0)]
        if original==color:
            return image
        def dfs(sr, sc):
            if sr<0 or sc<0 or sr>=rows or sc>=cols:
                return
            if image[sr][sc]!=original:
                return
            image[sr][sc]=color
            for dr,dc in dirs:
                dfs(sr+dr, sc+dc)

        dfs(sr,sc)
        return image
        