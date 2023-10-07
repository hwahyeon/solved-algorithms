def main():
    n = int(input())
    
    for _ in range(n):
        g, initialCandies, evolveCandies = map(int, input().split())
        candies = evolveCandies - initialCandies

        if g == 1:
            km = candies
        elif g == 2:
            km = 3 * candies
        else:
            km = 5 * candies

        if km <= 0:
            print(0)
        else:
            print(km)

if __name__ == "__main__":
    main()
