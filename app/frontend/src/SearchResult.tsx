import React from 'react';
import './SearchResult.css';

interface SearchResultProps {
    title: string;
    link: string;
    description: string;
    similarityScore: number;
}

const SearchResult: React.FC<SearchResultProps> = ({ title, link, description, similarityScore }) => {
    return (
        <div className="search-result">
            <h2 className="title">{title}</h2>
            <a href={link} className="link">{link}</a>
            <p className="description">{description}</p>
            <p className="similarity">Similarity Score: {similarityScore}</p>
        </div>
    );
};

export default SearchResult;