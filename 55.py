n = int(input())
english_subscribers = set(map(int, input().split()))

m = int(input())
french_subscribers = set(map(int, input().split()))

one_subscription_only = english_subscribers ^ french_subscribers
print(len(one_subscription_only))
