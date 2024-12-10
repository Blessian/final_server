import React from 'react';
import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper, CircularProgress, Box } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function RobotList() {
  const { data, isLoading, isError } = useQuery('robots', async () => {
    const response = await apiClient.getRobots();
    return response.data;
  });

  if (isLoading) {
    return <CircularProgress size={20} />;
  }

  if (isError) {
    return <Box sx={{ color: 'error.main' }}>Error loading robots</Box>;
  }

  return (
    <List sx={{ maxHeight: '200px', overflow: 'auto' }}>
      {data?.map((robot) => (
        <Paper key={robot.robot_id} sx={{ mb: 1 }}>
          <ListItem dense>
            <ListItemText
              primary={`Robot ID: ${robot.robot_id}`}
              secondary={`Status: ${robot.status}`}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default RobotList;