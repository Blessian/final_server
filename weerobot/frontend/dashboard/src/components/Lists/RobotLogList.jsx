import React from 'react';
import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper, CircularProgress } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function RobotLogList() {
  const { data, isLoading, isError } = useQuery('robotLogs', async () => {
    const response = await apiClient.getRobotLogs();
    return response.data;
  });

  if (isLoading) {
    return <CircularProgress />;
  }

  if (isError) {
    return <div>Error loading robot logs</div>;
  }

  return (
    <List>
      {data?.map((log) => (
        <Paper key={log.log_id} sx={{ mb: 1 }}>
          <ListItem>
            <ListItemText
              primary={`Log ID: ${log.log_id}`}
              secondary={`Robot ID: ${log.robot_id} | Status: ${log.status} | Time: ${new Date(log.registered).toLocaleString()}`}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default RobotLogList;