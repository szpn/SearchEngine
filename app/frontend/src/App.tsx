import React, { useState } from 'react';
import './App.css';
// @ts-ignore
import { ReactComponent as SearchIcon } from "./assets/search-icon.svg"
import SearchResult, { SearchResultProp } from './SearchResult';

const App: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState<SearchResultProp[]>([]);


    const dummySearchResults = [
        {
            title: 'Result 1',
            link: 'https://example.com',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            similarityScore: 0.75,
        },
        {
            title: 'Result 2',
            link: 'https://example.com',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            similarityScore: 0.12,
        },
    ];

    const handleSearch = () => {
         setSearchResults(dummySearchResults);
    };

    return (
        <div className="App">
            <div className="container">
                <h1 className="logo">Searchify</h1>
                <div className="search-box">
                    <input
                        type="text"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        placeholder="Search..."
                        className="search-input"
                    />
                    <button onClick={handleSearch} className="search-button">
                        <SearchIcon className="search-icon" />
                    </button>
                </div>
                <div className="search-results">
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
