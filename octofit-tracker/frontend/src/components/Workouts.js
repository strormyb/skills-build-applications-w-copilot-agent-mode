import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const endpoint = `${process.env.REACT_APP_API_BASE_URL}/workouts/`;
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Workouts endpoint:', endpoint);
        console.log('Fetched workouts:', results);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-header bg-secondary text-white">
        <h2 className="mb-0">Workouts</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Type</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, idx) => (
              <tr key={workout.id || idx}>
                <td>{workout.id || idx + 1}</td>
                <td>{workout.name || '-'}</td>
                <td>{workout.type || '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
