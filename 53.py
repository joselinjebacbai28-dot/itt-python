
n = int(input())
english_subscribers = set(map(int, input().split()))


m = int(input())
french_subscribers = set(map(int, input().split()))


only_english = english_subscribers - french_subscribers


print(len(only_english))
