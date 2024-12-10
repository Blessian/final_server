import React from 'react';
import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper, CircularProgress } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function CCTVLogList() {
  const { data, isLoading, isError } = useQuery('cctvLogs', async () => {
    const response = await apiClient.getCCTVLogs();
    return response.data;
  });

  if (isLoading) {
    return <CircularProgress />;
  }

  if (isError) {
    return <div>Error loading CCTV logs</div>;
  }

  return (
    <List>
      {data?.map((log) => (
        <Paper key={log.log_id} sx={{ mb: 1 }}>
          <ListItem>
            <ListItemText
              primary={`Log ID: ${log.log_id}`}
              secondary={`CCTV ID: ${log.cctv_id} | Time: ${new Date(log.registered).toLocaleString()}`}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default CCTVLogList;