import React from 'react';
import { Modal, Box } from '@mui/material';
import { useStore } from '../hooks/useStore';

function VideoModal() {
  console.log('VideoModal rendered'); // 디버깅용 로그
  const { videoModalOpen, setVideoModalOpen } = useStore();

  return (
    <Modal
      open={videoModalOpen}
      onClose={() => setVideoModalOpen(false)}
      aria-labelledby="video-modal"
    >
      <Box
        sx={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: '80%',
          bgcolor: 'background.paper',
          boxShadow: 24,
          p: 4,
        }}
      >
        <div>Video Content</div>
      </Box>
    </Modal>
  );
}

export default VideoModal;