import heapq


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        # Graph Representation
        # Create a graph of character conversions
        adjacency_list: list[list[tuple[int, int]]] = [[] for _ in range(26)]

        # Loop through all conversions
        conversion_count = len(original)
        for conversion_index in range(conversion_count):

            # Get the source and target character indices and the cost of conversion
            source_char_index = ord(original[conversion_index]) - ord("a")
            target_char_index = ord(changed[conversion_index]) - ord("a")
            conversion_cost = cost[conversion_index]

            # Append the conversion details to the graph
            adjacency_list[source_char_index].append(
                (target_char_index, conversion_cost)
            )

        # Shortest Path Calculation
        def dijkstra(
            start: int, adjacencyList: list[list[tuple[int, int]]]
        ) -> list[float]:
            """
            Perform Dijkstra's algorithm to find the minimum cost to convert the start
            character to all other characters.
            """

            # Create a priority queue to store characters with their conversion cost, sorted by cost
            priority_queue = [(0, start)]

            # Create a list to store the minimum conversion cost to each character
            min_costs = [float("inf")] * 26

            # Process the priority queue
            while priority_queue:
                current_cost, current_char = heapq.heappop(priority_queue)
                if min_costs[current_char] != float("inf"):
                    continue
                min_costs[current_char] = current_cost

                # Explore all possible conversions from the current character
                for target_char, conversion_cost in adjacencyList[current_char]:
                    new_total_cost = current_cost + conversion_cost

                    # If we found a cheaper conversion, update its cost
                    if min_costs[target_char] == float("inf"):
                        heapq.heappush(priority_queue, (new_total_cost, target_char))
            
            # Return the list of minimum conversion costs from the starting character to all others
            return min_costs

        # Calculate shortest paths for all possible character conversions
        min_conversion_costs = [
            dijkstra(start_char, adjacency_list) for start_char in range(26)
        ]

        # Cost Calculation
        # Calculate the total cost of converting source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                char_conversion_cost = min_conversion_costs[ord(s) - ord("a")][
                    ord(t) - ord("a")
                ]
                if char_conversion_cost == float("inf"):
                    return -1
                total_cost += int(char_conversion_cost)

        return total_cost
