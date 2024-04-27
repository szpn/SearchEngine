import React, {useEffect, useState} from 'react';
import SideBarComponent from './SideBarComponent';
import './Statistics.css';
// @ts-ignore
import { ReactComponent as StatisticsIcon } from "../../assets/statistics-icon.svg";

export interface SearchStatisticsData {
    creation_time: number;
    search_time: number;
}

interface SearchEngineData {
    article_count: number;
    dictionary_count: number;
}

const Statistics: React.FC<{ data: SearchStatisticsData }> = ({data}) => {
    const [searchEngineData, setSearchEngineData] = useState<SearchEngineData>({article_count: 0, dictionary_count: 0})
    
    useEffect(() => {
        fetch(`${process.env.REACT_APP_API_URL}/engine_statistics`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data: SearchEngineData)=>{
                console.log(data)
                setSearchEngineData(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            })
    }, []);
    
    return (
        <SideBarComponent
            title={"Statistics"}
            Icon={StatisticsIcon}
            content={
                <>
                    <div className="statistics-section" id="general-statistics">
                        <div className="statistic-item">
                            <span className="statistic-label">Articles count</span>
                            <span className="statistic-value">{searchEngineData.article_count}</span>
                        </div>
                        <div className="statistic-item">
                            <span className="statistic-label">Dictionary size:</span>
                            <span className="statistic-value">{searchEngineData.dictionary_count}</span>
                        </div>
                    </div>
                    <div className="statistics-section" id="time-statistics">
                        <div className="statistic-item">
                            <span className="statistic-label">Query time:</span>
                            <span className="statistic-value">{data.search_time.toPrecision(3)}</span>
                        </div>
                        <div className="statistic-item">
                            <span className="statistic-label">Description fetch time:</span>
                            <span className="statistic-value">{data.creation_time.toPrecision(3)}</span>
                        </div>
                    </div>
                </>
            }
        />
    );
};

export default Statistics;
