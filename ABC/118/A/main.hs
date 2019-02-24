main = do
  a <- getLine
  let b = map read (words a)
  let f = (b !! 0)
  let s = (b !! 1)

  let ans = if (s `mod` f == 0) then s + f else s - f

  print ans

