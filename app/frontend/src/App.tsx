import React, { useState, useEffect } from 'react';
import './App.css';
// @ts-ignore
import { ReactComponent as SearchIcon } from "./assets/search-icon.svg"
import SearchResult, { SearchResultProp } from './SearchResult';

const App: React.FC = () => {
    const [isSearching, setIsSearching] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState<SearchResultProp[]>([]);
    const dummySearchResults = [
        {
            title: 'Result 1',
            link: 'https://example.com',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            similarityScore: 0.75,
        },
        {
            title: 'Result 2',
            link: 'https://example.com',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            similarityScore: 0.12,
        },
                {
            title: 'Result 2',
            link: 'https://example.com',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            similarityScore: 0.12,
        },
                {
            title: 'Result 2',
            link: 'https://example.com',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            similarityScore: 0.12,
        },

    ];

    const handleSearch = () => {
        setIsSearching(true);
        setSearchResults(dummySearchResults);
    };

    const handleLogoClick = () => {
        setIsSearching(false);
        setSearchResults([]);
    };

    useEffect(() => {
        const handleScroll = (event : WheelEvent) => {
            const searchResultsDiv = document.querySelector('.search-results');
            console.log("Event details:", event);
            if (searchResultsDiv) {
                searchResultsDiv.scrollTop += event.deltaY;
            }
        };

        window.addEventListener('wheel', handleScroll);

        return () => {
            window.removeEventListener('wheel', handleScroll);
        };
    }, []);

    return (
        <div className="App">
            <div className="container">
                <h1 className={`logo ${isSearching ? 'searching' : ''}`} onClick={handleLogoClick}>Searchify</h1>
                <div className="search-box">
                    <input
                        type="text"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        placeholder="Search..."
                        className="search-input"
                    />
                    <button onClick={handleSearch} className="search-button">
                        <SearchIcon className="search-icon"/>
                    </button>
                </div>
                <div className="search-results" style={{height: isSearching ? '100%' : '0%'}}>
                    {searchResults.map((result, index) => (
                        <SearchResult
                            key={index}
                            title={result.title}
                            link={result.link}
                            description={result.description}
                            similarityScore={result.similarityScore}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default App;
