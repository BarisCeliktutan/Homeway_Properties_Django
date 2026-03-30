# # def timeConversion(s):
# #     h = int(s[0:2])
# #     print(s[-2])
# #     if s[-2] == "P" and h <= 12:
# #         rest = s[2:8]
# #         return f"{h+12}{rest}"
# #     else:
# #         return s[0:8]
    
# # print(timeConversion("12:05:39AM"))


# # def solve(arr):
# #     # Write your code here
# #     sorted_rev = sorted(arr)[::-1]
# #     sub_a = []
    
# #     for idx, i in enumerate(sorted_rev):
# #         sub_a.append(i)
# #         if sum(sub_a) > sum(sorted_rev[idx+1:]):
# #             return sorted(sub_a)

# # arr = [1,2,3,3,4,4,5,5,7]

# # print(solve(arr))



# # def countGroups(rows):
# #     def dfs(node, visited, adjacency_list):
# #         # Mark the current node as visited
# #         visited[node] = True
# #         # Visit all connected nodes
# #         for neighbor in adjacency_list[node]:
# #             if not visited[neighbor]:
# #                 dfs(neighbor, visited, adjacency_list)

# #     # Convert rows to an adjacency list
# #     n = len(rows)
# #     adjacency_list = {i: [] for i in range(n)}
# #     for i, row in enumerate(rows):
# #         for j, val in enumerate(row):
# #             if val == 1 and i != j:  # Add edges, but skip self-loops
# #                 adjacency_list[i].append(j)

# #     visited = [False] * n
# #     group_count = 0

# #     for i in range(n):
# #         if not visited[i]:
# #             # Start a new DFS traversal
# #             dfs(i, visited, adjacency_list)
# #             group_count += 1

# #     return group_count

# # print(countGroups([[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]))


# # def searchSuggestions(repository, customerQuery):
# #     rep = sorted(list(map(str.lower, repository)))
# #     customerQuery = customerQuery.lower()
# #     searching = customerQuery[0]
# #     appearances = []
# #     for letter in customerQuery[1:]:
# #         searching += letter
# #         appeared_ones = []
# #         for item in rep:
# #             # if searching == item[0:len(searching)] and len(appeared_ones) < 3:
# #             if item.startswith(searching) and len(appeared_ones) < 3:
# #                 appeared_ones.append(item)
# #         appearances.append(appeared_ones)

# #     return appearances
# # # rep = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# # # q = "mouse"

# # rep = ["abbS", "abc", "Abs", "bcs", "bdsa", "cdde", "rgb", "yjmm", "xxmm", "zeee"]
# # q = "abbs"

# # rep_low = list(map(str.lower, rep))
# # print(searchSuggestions(rep, q))


# from collections import Counter

# def rare_words_finder(text):
#     if not text:
#         return []
    
#     words = text.lower().split()  # Convert to lowercase and split by whitespace
#     word_counts = Counter(words)  # Count occurrences of each word
    
#     sorted_counts = sorted(word_counts.items(), key=lambda x: x[1])  # Sort by frequency
    
#     return sorted_counts[:5]  # Return the five least common words

# # Test cases
# print(rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks"))
# # Expected Output: [('hey', 1), ('there', 1), ('hot', 1), ('shot', 1), ('are', 1)]

# print(rare_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy"))
# # Expected Output: [('brown', 1), ('jumps', 1), ('over', 1), ('but', 1), ('quick', 2)]

# print(rare_words_finder(""))
# # Expected Output: []

# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# # write your for loop here

# for name in range(len(usernames)):
#     usernames[name] = usernames[name].lower().replace(" ", "_")

# print(usernames)
