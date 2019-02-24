
main = do
  head <- getLine
  tail <- getContents
  let contens = map tail (splitOn "\n" tail)


