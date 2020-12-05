import Data.List
import System.Environment
import System.FilePath


-- implemented most of the stuff before i found out about haskell's "standard library"


type Block = [String]
type Entry = (String, String)
type Passport = [Entry]


required :: [String]
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


split :: Eq a => a -> [a] -> [[a]]
split d s = case span (/= d) s of
  (x, _ : ts) -> x : split d ts
  (x, []    ) -> x : []


-- https://stackoverflow.com/a/23979003
sameElems :: Eq a => [a] -> [a] -> Bool
sameElems xs ys = null (xs \\ ys) && null (ys \\ xs)


blocks :: [String] -> [Block]
blocks [] = []
blocks ls = a' : blocks b
 where
  (a, b) = case span (/= "") ls of
    ([], b) -> ([], tail b)
    (a , b) -> (a, b)
  a' = concatMap (split ' ') a


entry :: String -> Entry
entry s = case split ':' s of
  [a, b] -> (a, b)


passport :: Block -> Passport
passport xs = map entry xs


checkPassport :: Passport -> Bool
checkPassport p = intersect (map fst p) required `sameElems` required


compute :: [String] -> Int
compute ls = length . (filter checkPassport) . (map passport) . blocks $ ls


main :: IO ()
main = do
  exePath <- getExecutablePath
  content <- readFile (replaceFileName exePath "input.txt")
  putStrLn . show . compute . lines $ content
