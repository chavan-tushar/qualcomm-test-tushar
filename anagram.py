import sys
from collections import defaultdict
from threading import Thread, Lock


class Anagrams:

    # Threads for adding data into dictionary
    no_of_threads = 3

    def __init__(self):
        try:
            with open("qualcomm-test-words.txt") as anagrams:
                self.words = anagrams.readlines()
        except FileNotFoundError:
            print("File Not Found: Please provide correct file name including its path. eg. /path_to_file/filename.txt")
            sys.exit(1)
        except Exception as e:
            print(f"An error occured: {e}")
            sys.exit(2)

        # Removing duplicate entries
        self.words = list(dict.fromkeys(self.words))

        self._similar_words = defaultdict(list)

        self.lines_per_thread = len(self.words) // Anagrams.no_of_threads
        self.threads = []
        self.lock = Lock()

        # Threads for adding data into _similar_words dictionary
        for t in range(Anagrams.no_of_threads):
            self.start_line = t * self.lines_per_thread
            self.end_line = len(self.words) if t == Anagrams.no_of_threads - 1 else (t+1) * self.lines_per_thread
            thread = Thread(target=self._create_similar_words_dict, args=(self.start_line, self.end_line, self.lock))

            self.threads.append(thread)
            thread.start()

        for thread in self.threads:
            thread.join()

    # Creating dictionary for anagrams
    def _create_similar_words_dict(self, start_line, end_line, lock) -> None:
        """
        Method _create_similar_words_dict will read all the values from qualcomm-test-words.txt file
        and it will store them in a dictionary. Key of dictionary will be in sorted format.
        """

        for word in self.words[start_line:end_line]:
            word = word.strip().lower()
            sorted_word = self._get_sorted_word(word)

            with lock:
                if sorted_word in self._similar_words.keys():
                    self._similar_words[self._get_sorted_word(word)].append(word)
                else:
                    self._similar_words[self._get_sorted_word(word)] = [word]

    # Checking type of input to get_anagrams method.
    def _check_input_format(self, word: any) -> None:
        if not isinstance(word, str):
            raise AttributeError(f"Input should be in string format.")

    # Returning anagrams from _similar_words dictionary
    def get_anagrams(self, word: str) -> list[str] | str:
        """
        Method get_anagrams returns the value from a dictionary

        Parameters:
            word (string): To find anagrams in qualcomm-test-words.txt file

        Returns:
            list[str] | str: list of Anagrams or error message
        """

        try:
            self._check_input_format(word)
        except AttributeError as e:
            return f"Invalid Input: {e}"
        else:
            word = word.strip()
            if len(word) == 0:
                return "Invalid Input: Please provide a word to check"

            if not word.isalpha():
                return f"Invalid Input: Entered word '{word}' is not a correct word. Please enter a correct word."

            word = self._get_sorted_word(word.lower())

            toReturn = self._similar_words.get(word)

            if not toReturn:
                return f"Could not find anagram word in qualcomm-test-words.txt file."
            
            return toReturn

    # Sorting input into alphabatical order
    def _get_sorted_word(self, word: str) -> str:
        """
        Method _get_sorted_word is used for getting a word in sorted alphabatical order

        Parameters:
            word (string): To sort the word in alphabatical order

        Returns:
            str: Word sorted in alphabatical order

        """
        return "".join(sorted(list(word)))


if __name__ == "__main__":
    a = Anagrams()
    print(a.get_anagrams("eat"))
    print(a.get_anagrams("plates"))
    
