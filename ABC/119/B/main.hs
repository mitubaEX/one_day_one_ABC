import Data.Text
check :: Double -> String -> Double
check a b = if b == "JPY"
               then a
               else a * 380000

main = do
  head <- getLine
  s <- getContents
  let cont = Prelude.map Prelude.words $ Prelude.map unpack (splitOn (pack "\n") (pack s))
  let fil = Prelude.filter (Prelude.not . Prelude.null) cont
  let ans = Prelude.sum $ Prelude.map (\x -> check (read (x !! 0) :: Double) (x !! 1)) fil
  print ans
