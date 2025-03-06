import time
import requests
import os
from dotenv import load_dotenv
import openai
import concurrent.futures


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

ANKI_API_URL = "http://localhost:8765"

master_dsa = {
    "Arrays": [
        "Find pair with given sum in the array",
        "Check if subarray with 0 sum exists; Print all subarrays with 0 sum",
        "Sort binary array in linear time",
        "Find a duplicate element in a limited range array",
        "Find largest subarray formed by consecutive integers",
        "Find maximum length subarray having given sum",
        "Find maximum length subarray having equal number of 0’s and 1’s",
        "Sort an array containing 0’s, 1’s and 2’s (Dutch National Flag problem)",
        "Inplace merge two sorted arrays",
        "Merge two arrays by satisfying given constraints",
        "Find index of 0 to be replaced to get maximum continuous ones",
        "Find maximum product of two integers in an array",
        "Shuffle an array (Fisher–Yates shuffle)",
        "Rearrange the array with alternate high and low elements",
        "Find equilibrium index of an array",
        "Find majority element in an array (Boyer–Moore algorithm)",
        "Move all zeros to the end",
        "Replace each element with product of every other element (without division)",
        "Find Longest Bitonic Subarray",
        "Find maximum difference between two elements satisfying constraints",
        "Maximum subarray problem (Kadane’s algorithm)",
        "Print continuous subarray with maximum sum",
        "Maximum Sum Circular Subarray",
        "Find all distinct combinations of given length",
        "Find all distinct combinations with repetition allowed",
        "Find maximum sequence of continuous 1’s by replacing at-most k zeros",
        "Find minimum sum subarray of given size k",
        "Find subarray having given sum",
        "Find the length of smallest subarray whose sum exceeds a target",
        "Find largest number possible from a set of given numbers",
        "Find the smallest window which, when sorted, makes the entire array sorted",
        "Find maximum sum path involving elements of given arrays",
        "Maximum profit earned by buying and selling shares (single/multiple transactions)",
        "Trapping Rain Water",
        "Longest Increasing Subsequence",
        "Longest Decreasing Subsequence",
        "Find maximum product subarray",
        "Find maximum sum of subsequence with no adjacent elements",
        "Find minimum platforms needed",
        "Decode the array constructed from another array",
        "Sort an array using one swap",
        "Find triplet with given sum in an array",
        "Length of longest continuous sequence with same sum in binary arrays",
        "Rearrange array such that A[A[i]] = i",
        "Reverse every consecutive m elements of a subarray",
        "Maximum Product Subset Problem",
        "Find pairs with given difference k in the array",
        "Find pairs with given difference k (constant space solution)",
        "4-sum problem (quadruplets with given sum)",
        "Print all quadruplets with given sum",
        "Find odd occurring element in an array in single traversal",
        "Find two odd occurring elements without extra space",
        "Quickselect Algorithm",
        "Print all triplets that form arithmetic progression",
        "Print all triplets that form geometric progression",
        "Print all combinations of numbers from 1 to n that sum to a given number",
        "Replace each element by its rank in the array",
        "Print all triplets in an array with sum ≤ given number",
        "Group elements based on first occurrence",
        "Find minimum difference between indices of two given elements",
        "Find maximum absolute difference between sum of two non-overlapping subarrays",
        "Find all symmetric pairs in an array of pairs",
        "Partition an array into two subarrays with the same sum",
        "Find count of distinct elements in every subarray of size k",
        "Find two numbers with maximum sum formed by array digits",
        "Print all subarrays of an array having distinct elements",
        "Find a triplet having maximum product in an array",
        "Find ways to calculate a target from elements of a specified array",
        "Find minimum index of repeating element",
        "Generate random input from an array according to given probabilities",
        "Find pair in an array having minimum absolute sum",
        "Find index of maximum occurring element with equal probability",
        "Check if an array is formed by consecutive integers",
        "Find two non-overlapping pairs having same sum",
        "Find minimum product among all combinations of triplets",
        "Replace every element with the least greater element on its right",
    ],
    "Strings": [
        "Longest Substring Without Repeating Characters",
        "Longest Repeating Character Replacement",
        "Smallest Window Containing All Characters",
        "Check for Anagram",
        "Print All Anagrams Together",
        "Check Balanced Parentheses",
        "Sentence Palindrome",
        "Longest Palindromic Substring",
        "Palindromic Substrings",
        "Longest Common Prefix",
        "Palindrome Check",
        "Reverse a String",
        "Reverse Words in a Given String",
        "Check for Rotation",
        "First Non-Repeating Character",
        "Roman Number to Integer",
        "Integer to Roman",
        "Closest Strings",
        "Divisible by 7",
        "Encrypt the String – II",
        "Equal Point in a String of Brackets",
        "Isomorphic Strings",
        "Check if Two Strings are K-Anagrams or Not",
        "Pangram Checking",
        "Minimum Deletions to Make a String Palindrome",
        "Number of Distinct Subsequences",
        "Implement Atoi",
        "License Key Formatting",
        "Find the Largest Word in Dictionary",
        "Count Equal 0s, 1s, and 2s in a String",
        "Find and Replace in String",
        "Add Binary Strings",
        "Sum of Two Large Numbers",
        "Multiply Two Strings",
        "Look and Say Pattern",
        "Minimum Times A has to be Repeated to Make B a Substring",
        "Excel Sheet Column Title",
        "Form a Palindrome",
        "Find the N-th Character of a Repeated String",
        "Next Higher Palindromic Number Using the Same Set of Digits",
        "Length of Longest Prefix Suffix",
        "Longest K Unique Characters Substring",
        "Smallest Window in a String Containing All Characters",
        "Longest Palindromic Subsequence",
        "Substrings of Length k with k-1 Distinct Elements",
        "Count Number of Substrings",
        "Interleaved Strings",
        "Rank the Permutation",
        "A Special Keyboard Problem",
        "Restrictive Candy Crush",
        "Edit Distance",
        "Search Pattern (KMP Algorithm)",
        "Search Pattern (Rabin-Karp Algorithm)",
        "Shortest Common Supersequence",
        "Number of Words with K Maximum Distinct Vowels",
        "Longest Substring to Form a Palindrome",
        "Longest Valid Parenthesis",
        "Distinct Palindromic Substrings",
    ],
    "Sorting": [
        "Insertion sort (Iterative & Recursive)",
        "Selection sort (Iterative & Recursive)",
        "Bubble sort (Iterative & Recursive)",
        "Merge Sort",
        "Iterative Merge Sort (Bottom-up)",
        "Quicksort (iterative, hybrid, Dutch National Flag, Hoare’s partition, external)",
        "Counting Sort",
        "Inversion Count",
        "Custom Sort (by frequency, by second array order)",
        "Segregate positive and negative integers in linear time",
        "Sort an array using one swap",
        "Sort a K-Sorted Array",
    ],
    "Searching": [
        "Binary Search",
        "Ternary Search",
        "Interpolation search",
        "Exponential search",
        "Find number of rotations in a circularly sorted array",
        "Search an element in a circular sorted array",
        "Find first/last occurrence in a sorted array",
        "Count occurrences in a sorted array with duplicates",
        "Find smallest missing element from a sorted array",
        "Find Floor and Ceil in a sorted array",
        "Search in a nearly sorted array",
        "Count number of 1’s in a sorted binary array",
        "Find the peak element in an array",
    ],
    "Matrix": [
        "Spiral Traversal",
        "Search in a sorted matrix",
        "Set Matrix Zeroes",
        "Transpose of a Matrix",
        "Word Search (in matrix)",
        "Search in a row-column sorted matrix",
        "Kth Element in Matrix",
        "Is Valid Sudoku",
        "Solve the Sudoku",
        "Spirally Traversing a Matrix",
        "Rotate Matrix Elements",
        "Sort the Given Matrix",
        "Turn an Image by 90°",
        "Multiply Two Matrices",
        "Print Matrix in Snake Pattern",
        "Sort a Matrix in All-Way Increasing Order",
        "Find the Row with Maximum Number of 1s",
        "Compute Diagonal Sums",
        "Boundary Elements of a Matrix",
        "Check if Matrix is Magic Square",
        "Find Peak Element in 2D Matrix",
        "Matrix Median",
        "Rotate a Matrix by 90° Without Extra Space",
        "Rotate a Matrix by 180°",
        "Rotate the Matrix Right by k Times",
        "Zigzag (Diagonal) Traversal of Matrix",
        "Find Number of Islands (in matrix)",
        "Boolean Matrix Question",
        "Maximum Sum Rectangle in 2D Matrix",
        "Count All Paths from Top Left to Bottom Right in M×N Matrix",
        "Find Maximum Sum Path in a Matrix",
        "Minimum Steps to Reach Target by a Knight",
        "Minimum Cost to Fill Given Weight in a Bag",
        "Shortest Path in a Binary Maze",
        "Maximum Size Rectangle Binary Sub-matrix with All 1s",
        "Find Largest Rectangular Area in a Histogram",
        "Find a Specific Pair in Matrix",
        "Maximum Size Square Sub-matrix with All 1s",
        "Largest Rectangle of 1s with Column Swaps Allowed",
        "Maximum Sum Rectangular Submatrix",
        "Minimum Initial Points to Reach Destination",
        "Count Number of Paths with At-Most k Turns",
        "Construct Ancestor Matrix from a Binary Tree",
        "Print k-th Element in Spiral Form of Matrix",
        "Find Size of the Largest '+' Formed by All Ones in a Binary Matrix",
        "Print Maximum Sum Square Sub-matrix of Given Size",
        "Validity of a Tic-Tac-Toe Board",
    ],
    "Hashing": [
        "Print all pairs with given sum",
        "Longest subsequence with adjacent difference 0 or 1",
        "Longest Consecutive Sequence",
        "Count subarrays with given XOR",
    ],
    "Two Pointer Technique": [
        "Triplet Sum",
        "Longest Substring With Distinct Characters",
        "Trapping Rain Water",
    ],
    "Prefix Sum": [
        "Longest subarray with equal number of 0s and 1s",
        "Product of array except self",
        "Find starting petrol pump for circular tour",
    ],
    "Linked List": [
        "Print the middle of a linked list",
        "Reverse a linked list",
        "Reverse a doubly linked list",
        "Rotate a linked list",
        "Nth node from the end",
        "Delete last occurrence",
        "Delete middle node",
        "Remove duplicates from sorted linked list",
        "Detect loop in linked list",
        "Delete N nodes after M nodes",
        "Merge a linked list into another at alternate positions",
        "Circular linked list traversal",
        "Deletion from circular linked list",
        "Delete without head pointer",
        "Implement queue using linked list",
        "Implement stack using singly linked list",
        "Remove every k-th node",
        "Pairwise swap",
        "Count occurrences in linked list",
        "Sort linked list of 0s, 1s, and 2s",
        "Deletion in linked list",
        "Convert singly linked list into circular linked list",
        "Reverse linked list in groups of given size",
        "Merge two sorted linked lists",
        "Remove loop in linked list",
        "Check if linked list is palindrome",
        "Remove all occurrences of one linked list from another",
        "Intersection point in Y-shaped linked lists",
        "Intersection of two sorted linked lists",
        "Split a circular linked list into two halves",
        "Find pairs with given sum in doubly linked list",
        "Remove duplicates from unsorted doubly linked list",
        "Intersection point of two linked lists",
        "Add two numbers represented by linked lists",
        "Multiply two numbers represented by linked lists",
        "Swap k-th node from beginning with k-th node from end",
        "Sort a k-sorted doubly linked list",
        "Rotate doubly linked list by n nodes",
        "Convert a binary tree into doubly linked list (spiral)",
        "Convert a binary tree to doubly linked list",
        "Construct a linked list from 2D matrix",
        "Reverse a doubly linked list in groups of given size",
        "Reverse a sublist of linked list",
        "Rearrange linked list in-place",
        "Reverse alternate k nodes in a singly linked list",
        "Merge k sorted linked lists",
        "Flatten a linked list",
        "Partition a linked list around a given value",
        "Clone a linked list with random pointers",
    ],
    "Backtracking": [
        "Print all solutions to N Queens",
        "Print all Knight’s Tours",
        "Find shortest path in maze",
        "Find longest possible route in a matrix",
        "Find path from source to destination in matrix with constraints",
        "Count total unique paths in a maze",
        "Print all Hamiltonian paths in a graph",
        "Print all k-colorable configurations (vertex coloring)",
        "Find all permutations of a given string",
        "Print all binary strings from a wildcard pattern",
        "K-Partition Problem: Print all partitions",
        "Magnet Puzzle",
        "Find ways to calculate a target from elements of specified array",
        "Find minimum number possible with at-most K swaps",
        "Determine if a pattern matches with a string",
    ],
    "Binary": [
        "Bit Hacks – Part 1: Basic",
        "Bit Hacks – Part 2: Playing with k-th bit",
        "Bit Hacks – Part 3: Rightmost set bit",
        "Bit Hacks – Part 4: Letters of English alphabet",
        "Bit Hacks – Part 5: Find absolute value without branching",
        "Bit Hacks – Part 6: Random Problems",
        "Brian Kernighan’s Algorithm to count set bits",
        "Compute parity using lookup table",
        "Count set bits using lookup table",
        "Find minimum or maximum of two integers without branching",
        "Multiply 16-bit integers using an 8-bit multiplier",
        "Round up to next highest power of 2",
        "Round up to previous power of 2",
        "Swap individual bits at given position",
        "Check if number is power of 4",
        "Reverse bits of an integer",
        "Swap two bits at given position",
        "Add binary representation of two integers",
        "Swap adjacent bits of a number",
        "Print all distinct subsets of a given set",
        "Perform division without using / operator",
        "Check if adjacent bits are set",
        "Conditionally negate a value without branching",
        "Find two duplicate elements using XOR",
        "Find missing number and duplicate elements",
        "Check if number is power of 8",
        "Circular shift on binary representation by k positions",
        "Solve problems without using multiplication or division",
        "Reverse bits using lookup table",
        "Generate binary numbers between 1 to N",
        "Efficiently implement power function (recursive & iterative)",
        "Find square of a number without multiplication",
        "Generate power set of a given set",
        "Huffman Coding",
        "Find all odd occurring elements in a limited range array",
    ],
    "Binary Tree": [
        "Check if two binary trees are identical (iterative & recursive)",
        "Calculate height of a binary tree (iterative & recursive)",
        "Delete a binary tree (iterative & recursive)",
        "Inorder tree traversal (iterative & recursive)",
        "Preorder tree traversal (iterative & recursive)",
        "Postorder tree traversal (iterative & recursive)",
        "Level order traversal",
        "Spiral order traversal",
        "Reverse level order traversal",
        "Print all nodes in a specific order",
        "Print left view of binary tree",
        "Print bottom view of binary tree",
        "Print top view of binary tree",
        "Find next node in same level",
        "Check if binary tree is complete",
        "Determine if two nodes are cousins",
        "Print cousins of a given node",
        "Convert binary tree to sum tree (in-place)",
        "Check if binary tree is a sum tree",
        "Mirror (invert) binary tree",
        "Subtree check",
        "Diameter of binary tree",
        "Symmetric tree check",
        "Find Lowest Common Ancestor (LCA)",
        "Print all root-to-leaf paths",
        "Print ancestors of a given node",
        "Vertical traversal",
        "Diagonal sums/traversals",
        "Convert binary tree to doubly linked list",
        "Additional advanced binary tree problems",
    ],
    "BST": [
        "Insertion in BST",
        "Search in BST",
        "Deletion in BST",
        "Construct balanced BST from given keys",
        "Determine if a binary tree is a BST",
        "Check if two BSTs are the same (without building BST)",
        "Find inorder predecessor in BST",
        "Find Lowest Common Ancestor (LCA) in BST",
        "Find k-th smallest/largest element in BST",
        "Floor and Ceil in BST",
        "Find optimal cost to construct BST",
        "Convert binary tree to BST (maintaining structure)",
        "Remove nodes from BST outside given range",
        "Find pair with given sum in BST",
        "Find inorder successor in BST",
        "Replace each element with least greater element on its right",
    ],
    "Divide & Conquer": [
        "Binary Search",
        "Find number of rotations in a circularly sorted array",
        "Search in circular sorted array",
        "Find first/last occurrence in sorted array",
        "Count occurrences in sorted array with duplicates",
        "Find smallest missing element in sorted array",
        "Find floor and ceil in sorted array",
        "Search in nearly sorted array",
        "Count number of 1’s in a sorted binary array",
        "Find the peak element in an array",
        "Maximum Sum Subarray using Divide & Conquer",
        "Find minimum and maximum element using minimum comparisons",
        "Implement power function (recursive & iterative)",
        "Find missing term in a sequence (log n time)",
        "Division of two numbers using binary search",
        "Find frequency of each element in sorted array with duplicates",
        "Ternary Search vs Binary Search",
        "Exponential search",
        "Interpolation search",
        "Merge Sort",
        "Iterative Merge Sort (Bottom-up)",
        "Merge Sort for singly linked list",
        "Inversion Count of an array",
        "Quicksort Algorithm",
        "Iterative Implementation of Quicksort",
        "Hybrid QuickSort",
        "Quicksort using Dutch National Flag Algorithm",
        "Quick Sort using Hoare’s Partitioning",
        "External merge sort",
        "Custom Sort (by frequency, by second array order)",
        "Segregate positive and negative integers",
        "Efficiently implement power function",
        "Merge two sorted arrays in-place (using one swap)",
    ],
    "Dynamic Programming": [
        "Nth Catalan Number",
        "Minimum Operations",
        "Minimum Steps to Delete Using Palindrome Substrings",
        "Minimum Number of Coins",
        "Maximum Product Cutting",
        "Ways to Cover a Distance",
        "Minimum Deletions and Insertions to Transform a String",
        "Minimum Sum Subsequence (one of every four consecutive elements)",
        "Subset Sum Problem",
        "Longest Common Subsequence",
        "Longest Increasing Subsequence",
        "Edit Distance",
        "Longest Path in Matrix",
        "0–1 Knapsack Problem",
        "Shortest Common Supersequence",
        "Partition Problem",
        "Rod Cutting",
        "Coin Change Problem (number of ways)",
        "Word Break Problem",
        "Dice Throw Problem",
        "Box Stacking",
        "Egg Dropping Puzzle",
        "Maximum Length Chain",
        "Longest Common Substring",
        "Interleaved Strings",
        "Maximum Sum Increasing Subsequence",
        "Minimum Number of Jumps to Reach End",
        "Count Subsequences of type a^i, b^j, c^k",
        "Get Minimum Squares",
        "Nth Fibonacci Number",
        "Longest Palindromic Substring",
        "Total Decoding Messages",
        "Unique BSTs",
        "Player with Maximum Score",
        "Form a Palindrome",
        "Word Wrap Problem",
        "Count Palindromic Subsequences",
        "Minimum Time to Finish Tasks Without Skipping Two Consecutive",
        "Minimum Partition",
        "Boolean Parenthesization Problem",
        "Matrix Chain Multiplication",
        "Longest Zig-Zag Subsequence",
        "Maximum Profit in Job Scheduling",
        "Maximum Path Sum in Matrix",
        "The Painter’s Partition Problem",
        "Palindrome Partitioning",
        "Array Partition",
        "Maximum Difference of Zeros and Ones in Binary String",
        "Count Digit Groupings of a Number",
    ],
    "Greedy": [
        "Minimum Platforms",
        "Job Sequencing with Deadlines",
        "Activity Selection",
        "Huffman Coding",
        "Shortest Superstring Problem",
        "Greedy Graph Coloring",
        "Kruskal’s Algorithm",
        "Dijkstra’s Algorithm",
    ],
    "Graphs": [
        "Print Adjacency List",
        "BFS of Graph",
        "DFS of Graph",
        "Transitive Closure of a Graph",
        "Union-Find",
        "Detect Cycle using DSU",
        "Connected Components in Undirected Graph",
        "Find number of islands",
        "Detect Cycle in Undirected Graph",
        "Hamiltonian Path",
        "Course Schedule / Prerequisite Tasks",
        "Circle of Strings",
        "Snake and Ladder Problem",
        "Bipartite Graph",
        "Maximum Bipartite Matching",
        "Detect Cycle in Directed Graph",
        "Find whether a path exists",
        "Topological Sort",
        "Level of Nodes",
        "Possible Paths between Two Vertices",
        "Find number of ‘X’ total shapes",
        "Distance of nearest cell having 1",
        "Mother Vertex",
        "Unit area of largest region of 1’s",
        "Rotten Oranges",
        "Minimum Swaps to Sort",
        "Steps by Knight",
        "Implementing Dijkstra’s Algorithm",
        "Neeman’s Shoes",
        "Minimum Spanning Tree",
        "Strongly Connected Components (Kosaraju’s Algorithm)",
        "Bridge Edge in Graph",
        "Flood Fill Algorithm",
        "Replace O’s with X’s",
        "Shortest Prime Path",
        "Word Search (graph version)",
        "Construct Binary Palindrome by Repeated Appending and Trimming",
        "Word Boggle",
        "Critical Connections",
        "Minimum Cost Path",
        "Strongly Connected Components (Tarjan’s Algorithm)",
        "Articulation Point – I",
        "Articulation Point – II",
        "Alien Dictionary",
        "Word Ladder I",
        "Word Ladder II",
        "Find number of closed islands",
        "Shortest Path by Removing k Walls",
        "Minimum Length String with All Substrings of Size n",
    ],
    "Trie": [
        "Trie Implementation (Insert, Search, Delete)",
        "Memory efficient Trie Implementation using Map",
        "C++ Implementation of Trie",
        "Longest Common Prefix using Trie",
        "Lexicographic sorting of keys",
        "Find maximum/first k maximum occurring words",
        "Word Break Problem using Trie",
    ],
    "Puzzles": [
        "Clock angle problem — Find angle between hour and minute hand",
        "Add two numbers without using addition operator (4 methods)",
        "Generate power set of a given set",
        "Implement power function without using multiplication and division",
        "Print all numbers from 1 to N without using semicolon",
        "Swap two numbers without using a third variable (5 methods)",
        "Determine condition to print specific output",
        "Find maximum and minimum of three numbers without conditionals (4 methods)",
        "Find numbers as sum of two cubes for two different pairs",
        "Print 'Hello World' with an empty main() function (3 methods)",
        "Tower of Hanoi",
        "Print numbers from 1 to N without using any loop (4 methods)",
        "Print a semicolon without using semicolon anywhere",
        "Multiply two numbers without using multiplication operator or loops",
        "Find square of a number without using multiplication/division (3 methods)",
        "Check if a number is even or odd without using conditional statements",
        "Set both elements of a binary array to 0 in one line",
        "Find minimum number without using conditionals or ternary operator",
        "Perform division without using / operator",
        "Generate 0 and 1 with 75% and 25% probability",
        "Generate desired random numbers with equal probability",
        "Return 0, 1, and 2 with equal probability using a function",
        "Generate fair results from a biased coin",
        "Generate numbers from 1 to 7 with equal probability",
        "Implement ternary operator without using conditionals",
        "Determine if two integers are equal without using comparison operators",
        "Return 0 and 1 with equal probability using a function",
        "Generate random input from an array according to given probabilities",
        "Magnet Puzzle",
    ],
}


def fetch_openai_response(prompt, model="gpt-4o", response_format=None):
    """Fetches response from OpenAI API given a prompt and model."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            response_format=response_format,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return None


def rephrase_question(question):
    prompt = f"Elaborate this question in a leetcode style question: {question} add multiple different test cases in all scenarios"
    return fetch_openai_response(prompt, model="gpt-4o-mini")


def generate_solution(question):
    prompt = f"""
    Explain the solution, thought process, and intuition behind this concept in a way that helps me recognize patterns and deeply understand the underlying principles.
    I want to develop strong intuition and problem-solving skills to apply this knowledge across different scenarios.  
    However, don't just use words and assume I already understand them—break it down thoroughly.
    Explain why this solution even works, the core idea behind it, and how each step connects.
    Provide a clear step-by-step breakdown, along with code examples, to illustrate the approach effectively.
    Additionally, include strategies on how to recognize similar problems and master this concept over time.

    Start with a Brute Force Approach: Develop a simple, correct solution as a baseline, even if it's inefficient.
    Identify Inefficiencies: Analyze the solution to find performance bottlenecks.
    Incrementally Optimize: Replace inefficient parts with more efficient algorithms or data structures
    Explain Each Change: Provide a brief rationale for each optimization, focusing on performance improvements.
    Iterate Until Optimal: Continue refining until the solution is as efficient as possible.

    # coding problem statement
    {question}
    """
    return fetch_openai_response(prompt)


def create_anki_flashcard(deck_name, front, back, api_url=ANKI_API_URL):
    """Creates a flashcard in Anki using the provided front, back."""
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "KaTeX and Markdown Basic",
                "fields": {"Front": front, "Back": back},
                "options": {"allowDuplicate": False},
            }
        },
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        result = response.json()

        if result.get("error") is None:
            print(f"✅ Flashcard added successfully: {result}")
        else:
            print(f"❌ Error: {result['error']}")
    except requests.RequestException as e:
        print(f"❌ Failed to connect to Anki: {e}")


def process(question):
    start = time.time()

    print(f"\nProcessing question: {question}")
    print("\n========== writing question ==========")
    front = rephrase_question(question)
    print("\n[written question]\n", front)

    print("\n========== generating solution ==========")
    back = generate_solution(question)
    print("\n[generated solution]\n", back)

    DECK_NAME = "master dsa"
    create_anki_flashcard(DECK_NAME, front=front, back=back)

    end = time.time()
    print(f"Processing of question '{question}' took {end - start:.2f} seconds\n")


if __name__ == "__main__":
    total = sum(len(problems) for problems in master_dsa.values())
    current_index = 1

    # Dynamically set the maximum number of threads for I/O-bound tasks
    max_workers = (os.cpu_count() or 1) * 5

    overall_start = time.time()  # Start overall timing

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for ds, problems in master_dsa.items():
            for problem in problems:
                print(f"Scheduling processing for {current_index} out of {total}")
                question = f"{ds}: {problem}"
                # Submit the process function for concurrent execution
                futures.append(executor.submit(process, question))
                current_index += 1

        # Wait for all tasks to complete and handle exceptions if any
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # This will re-raise any exceptions caught during execution
            except Exception as e:
                print(f"Task generated an exception: {e}")

    overall_end = time.time()  # End overall timing
    print(f"\nTotal time taken: {overall_end - overall_start:.2f} seconds")
