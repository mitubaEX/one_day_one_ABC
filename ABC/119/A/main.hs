import Data.Text
main = do
  s <- getLine
  let date = Prelude.map unpack (splitOn (pack "/") (pack s))
  let ans = if (read (date !! 0)) <= 2019 && (read (date !! 1)) <= 4 && (read (date !! 2)) <= 30
               then "Heisei"
               else "TBD"
  putStrLn ans
