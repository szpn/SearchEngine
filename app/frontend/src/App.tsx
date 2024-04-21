import React, { useState } from 'react';
import './App.css';
// @ts-ignore
import { ReactComponent as SearchIcon } from "./assets/search-icon.svg"

const App: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState('');

    const handleSearch = () => {
        setSearchResults(searchTerm);
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
                    {searchResults && <p>Search results for: {searchResults}</p>}
                </div>
            </div>
        </div>
    );
};

export default App;
