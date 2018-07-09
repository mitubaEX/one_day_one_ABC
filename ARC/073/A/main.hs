import Control.Applicative

main = do
  [n,t] <- map read . words <$> getLine :: IO[Int]
  xs <- map read . words <$> getLine
  let ss = foldl (\(a, b) x -> (a + min n (x + t - b), x + t)) (0, 0) xs
  print ss
