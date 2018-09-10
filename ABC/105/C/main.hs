check :: Int -> String
check a = show a

main :: IO ()
main = do
  x <- check <$> readLn
  print x
