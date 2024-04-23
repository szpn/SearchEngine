import React from 'react';
import './SearchResult.css';

export interface SearchResultProp {
    name: string;
    url: string;
    description: string;
    similarity: number;
}

const SearchResult: React.FC<SearchResultProp> = ({ name, url, description, similarity }) => {
    return (
        <div className="search-result">
            <h2 className="title">{name}</h2>
            <p className="similarity">Similarity Score: {similarity.toFixed(3)}</p>
            <a href={url} className="link">{url}</a>
            <p className="description">{description}</p>
        </div>
    );
};

export default SearchResult;
