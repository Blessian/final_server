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

  // 최대 5개만 표시
  const displayData = data?.slice(0, 5) || [];

  return (
    <List disablePadding>
      {displayData.map((robot) => (
        <Paper key={robot.robot_id} sx={{ mb: 0.5 }}>
          <ListItem dense>
            <ListItemText
              primary={`Robot ID: ${robot.robot_id}`}
              secondary={`Status: ${robot.status}`}
              primaryTypographyProps={{ fontSize: '0.9rem' }}
              secondaryTypographyProps={{ fontSize: '0.8rem' }}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default RobotList;