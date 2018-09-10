-- 5,000,000,000,000,000

check :: [Char] -> Char
check (x:xs)
  | x == '1' = check xs
  | otherwise = x

main = do
  s <- getLine
  k <- getLine
  putChar $ if all (\x -> x == '1') s then '1' else check s

