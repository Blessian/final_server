import React from 'react';
import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper, CircularProgress, Box } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function RobotLogList() {
  const { data, isLoading, isError } = useQuery('robotLogs', async () => {
    const response = await apiClient.getRobotLogs();
    return response.data;
  });

  if (isLoading) {
    return <CircularProgress size={20} />;
  }

  if (isError) {
    return <Box sx={{ color: 'error.main' }}>Error loading robot logs</Box>;
  }

  // 최대 5개만 표시
  const displayData = data?.slice(0, 5) || [];

  return (
    <List disablePadding>
      {displayData.map((log) => (
        <Paper key={log.log_id} sx={{ mb: 0.5 }}>
          <ListItem dense>
            <ListItemText
              primary={`Log ID: ${log.log_id}`}
              secondary={`Robot ID: ${log.robot_id} | Status: ${log.status} | Time: ${log.registered}`}
              primaryTypographyProps={{ fontSize: '0.9rem' }}
              secondaryTypographyProps={{ fontSize: '0.8rem' }}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default RobotLogList;