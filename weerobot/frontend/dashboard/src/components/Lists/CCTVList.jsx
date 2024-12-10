import { useQuery } from 'react-query';
import { List, ListItem, ListItemText, Paper } from '@mui/material';
import { apiClient } from '../../api/apiClient';

function CCTVList() {
  const { data: cctvs, isLoading } = useQuery('cctvs', apiClient.getCCTVs);

  if (isLoading) return 'Loading...';

  return (
    <List>
      {cctvs?.data.map((cctv) => (
        <Paper key={cctv.cctv_id} sx={{ mb: 1 }}>
          <ListItem>
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