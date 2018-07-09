check :: String -> Bool
check a = a == reverse a

output :: Bool -> String
output True = "Yes"
output False = "No"

main = do
  n <- getLine
  let c = check n
  putStrLn $ output c
