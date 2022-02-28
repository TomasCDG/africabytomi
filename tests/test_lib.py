from bbquote.lib import get_quote

def test_quote_none():

    quote = get_quote()

    assert quote != None

def test_quote_africa():

    quote = get_quote()

    assert "africa" in quote.lower()