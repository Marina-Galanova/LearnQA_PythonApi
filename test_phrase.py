class TestPhrase:
    def test_leght_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Фраза больше 15 символов"

