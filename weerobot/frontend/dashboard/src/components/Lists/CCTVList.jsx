import React from 'react';
import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper, CircularProgress, Box } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function CCTVList() {
  const { data, isLoading, isError } = useQuery('cctvs', async () => {
    const response = await apiClient.getCCTVs();
    return response.data;
  });

  if (isLoading) {
    return <CircularProgress size={20} />;
  }

  if (isError) {
    return <Box sx={{ color: 'error.main' }}>Error loading CCTVs</Box>;
  }

  // 최대 5개만 표시
  const displayData = data?.slice(0, 5) || [];

  return (
    <List disablePadding>
      {displayData.map((cctv) => (
        <Paper key={cctv.cctv_id} sx={{ mb: 0.5 }}>
          <ListItem dense>
            <ListItemText
              primary={`CCTV ID: ${cctv.cctv_id}`}
              secondary={`Index: ${cctv.cctv_idx} | Location: ${cctv.latitude}, ${cctv.longitude}`}
              primaryTypographyProps={{ fontSize: '0.9rem' }}
              secondaryTypographyProps={{ fontSize: '0.8rem' }}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default CCTVList;