import unittest

class TestTrie(unittest.TestCase):

    def test_search_in_empty_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("apple"))  # Trie is empty, should return False
        self.assertFalse(trie.startsWith("app"))  # Trie is empty, should return False

    def test_insert_word(self):
        trie = Trie()
        trie.insert("apple")
        # No return value expected from insert, just verifying no exceptions occur

    def test_search_for_inserted_word(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))  # Should return True, as "apple" was inserted

    def test_search_for_non_existent_word(self):
        trie = Trie()
        trie.insert("apple")
        self.assertFalse(trie.search("banana"))  # Should return False, as "banana" was not inserted

    def test_search_for_prefix_of_existing_word(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.startsWith("app"))  # Should return True, as "app" is a prefix of "apple"

    def test_insert_another_word_with_common_prefix(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")
        self.assertTrue(trie.search("app"))  # Should return True, as "app" was inserted

    def test_search_for_newly_inserted_word(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")
        self.assertTrue(trie.search("app"))  # Should return True, as "app" was inserted

    def test_complex_sequence_of_operations(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")
        self.assertTrue(trie.search("apple"))  # Should return True
        self.assertTrue(trie.search("app"))    # Should return True
        self.assertTrue(trie.startsWith("app"))  # Should return True
        trie.insert("banana")
        self.assertTrue(trie.search("banana"))  # Should return True, as "banana" was inserted

if __name__ == "__main__":
    unittest.main()