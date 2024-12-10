import create from 'zustand';

export const useStore = create((set) => ({
  videoModalOpen: false,
  currentVideo: null,
  setVideoModalOpen: (isOpen) => set({ videoModalOpen: isOpen }),
  setCurrentVideo: (video) => set({ currentVideo: video }),
}));