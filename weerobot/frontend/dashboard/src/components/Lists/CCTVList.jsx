// CCTVList.jsx와 비슷한 구조로 다른 리스트 컴포넌트들도 수정
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

  return (
    <List sx={{ maxHeight: '200px', overflow: 'auto' }}>
      {data?.map((cctv) => (
        <Paper key={cctv.cctv_id} sx={{ mb: 1 }}>
          <ListItem dense>
            <ListItemText
              primary={`CCTV ID: ${cctv.cctv_id}`}
              secondary={`Index: ${cctv.cctv_idx} | Location: ${cctv.latitude}, ${cctv.longitude}`}
            />
          </ListItem>
        </Paper>
      ))}
    </List>
  );
}

export default CCTVList;