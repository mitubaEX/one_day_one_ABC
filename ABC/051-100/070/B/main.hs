import Control.Applicative

check :: Bool -> Bool -> (Integer -> Integer -> Integer -> Integer -> Integer)
check True True = \a b c d -> d - a
check True False = \a b c d -> d - c
check False True = \a b c d -> b - a
check False False = \a b c d -> b - c

main = do
  [a,b,c,d] <- map read . words <$> getLine
  let flag1 = b > d
  let flag2 = a > c
  let f = check flag1 flag2
  print $ max 0 $ f a b c d
