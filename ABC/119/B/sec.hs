check :: Double -> String -> Double
check a b = if b == "JPY"
               then a
               else a * 380000

main = do
  head <- getLine
  s <- getContents
  let cont = map words . lines $ s
  let ans = sum $ map (\x -> check (read (x !! 0) :: Double) (x !! 1)) cont
  print ans

