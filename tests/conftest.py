"""Pytest configuration and shared fixtures."""

import os

import pytest


@pytest.fixture
def sample_post_data():
    """Sample post data for testing."""
    return {
        "id": 12345,
        "slug": "bitcoin-reaches-new-high",
        "title": "Bitcoin Reaches New All-Time High",
        "description": "Bitcoin has reached a new all-time high of $100,000",
        "published_at": "2024-01-15T10:30:00Z",
        "created_at": "2024-01-15T10:25:00Z",
        "kind": "news",
        "source": {
            "title": "CoinDesk",
            "region": "en",
            "domain": "coindesk.com",
            "type": "feed",
        },
        "original_url": "https://www.coindesk.com/bitcoin-reaches-new-high",
        "url": "https://cryptopanic.com/news/12345/bitcoin-reaches-new-high/",
        "image": "https://cryptopanic.com/images/bitcoin.jpg",
        "instruments": [
            {
                "code": "BTC",
                "title": "Bitcoin",
                "slug": "bitcoin",
                "url": "https://cryptopanic.com/api/developer/v2/coins/btc/",
                "market_cap_usd": 2000000000000.0,
                "price_in_usd": 100000.0,
                "price_in_btc": 1.0,
                "price_in_eth": 20.0,
                "price_in_eur": 90000.0,
                "market_rank": 1,
            }
        ],
        "votes": {
            "negative": 5,
            "positive": 100,
            "important": 10,
            "liked": 50,
            "disliked": 5,
            "lol": 2,
            "toxic": 1,
            "saved": 25,
            "comments": 15,
        },
        "panic_score": 75,
        "panic_score_1h": 80,
        "author": "John Doe",
        "content": {
            "original": "<p>Bitcoin has reached...</p>",
            "clean": "Bitcoin has reached a new all-time high...",
        },
    }


@pytest.fixture
def sample_posts_response(sample_post_data):
    """Sample posts response data for testing."""
    return {
        "next": "https://cryptopanic.com/api/developer/v2/posts/?page=2",
        "previous": None,
        "results": [sample_post_data],
    }


@pytest.fixture
def empty_posts_response():
    """Empty posts response for testing."""
    return {
        "next": None,
        "previous": None,
        "results": [],
    }


@pytest.fixture
def auth_token():
    """Get auth token from environment variable or use test token.

    For unit tests, uses a dummy token since requests are mocked.
    For integration tests, reads from CRYPTOPANIC_AUTH_TOKEN env var.
    """
    return os.getenv("CRYPTOPANIC_AUTH_TOKEN", "test_token")
