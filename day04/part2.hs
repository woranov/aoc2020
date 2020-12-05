import Data.List
import qualified Data.Map as M
import System.Environment
import System.FilePath

type Block = [String]

type Entry = (String, String)

type Passport = M.Map String String

checkRange :: Int -> Int -> Int -> Bool
checkRange lo hi n = lo <= n && n <= hi

hexchars :: String
hexchars = "0123456789abcdef"

eyecolors :: [String]
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

height :: String -> (String, Int)
height s = (reverse revUnit, read (reverse revN))
  where
    (revUnit, revN) = splitAt 2 $ reverse s

containedIn :: Eq a => [a] -> a -> Bool
containedIn l x = x `elem` l

rules :: M.Map String (String -> Bool)
rules =
  M.fromList
    [ ("byr", (checkRange 1920 2002 .) $ read),
      ("iyr", (checkRange 2010 2020 .) $ read),
      ("eyr", (checkRange 2020 2030 .) $ read),
      ( "hgt",
        \s -> case height s of
          ("cm", n) -> checkRange 150 193 n
          ("in", n) -> checkRange 59 76 n
          _ -> False
      ),
      ("hcl", \s -> ("#" == take 1 s) && all (containedIn hexchars) (drop 1 s)),
      ("ecl", containedIn eyecolors),
      ("pid", \s -> length s == 9)
    ]

split :: Eq a => a -> [a] -> [[a]]
split d s = case span (/= d) s of
  (x, _ : ts) -> x : split d ts
  (x, []) -> x : []

-- https://stackoverflow.com/a/23979003
sameElems :: Eq a => [a] -> [a] -> Bool
sameElems xs ys = null (xs \\ ys) && null (ys \\ xs)

entry :: String -> Entry
entry s = case split ':' s of
  [a, b] -> (a, b)

blocks :: [String] -> [Block]
blocks [] = []
blocks ls = a' : blocks b
  where
    (a, b) = case span (/= "") ls of
      ([], b) -> ([], tail b)
      (a, b) -> (a, b)
    a' = concatMap (split ' ') a

passport :: Block -> Passport
passport xs = M.fromList $ map entry xs

containsRequired :: Passport -> Bool
containsRequired p = intersect (map fst $ M.toList p) (M.keys rules) `sameElems` (M.keys rules)

checkPassportEntry :: Entry -> Bool
checkPassportEntry (k, v) = case M.lookup k rules of
  Just r -> r v
  Nothing -> True

checkPassport :: Passport -> Bool
checkPassport p = containsRequired p && all checkPassportEntry (M.toList p)

compute :: [String] -> Int
compute ls = length . (filter checkPassport) . (map passport) . blocks $ ls

main :: IO ()
main = do
  exePath <- getExecutablePath
  content <- readFile (replaceFileName exePath "input.txt")
  putStrLn . show . compute . lines $ content
