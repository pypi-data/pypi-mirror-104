from hypothesis import given, strategies as st

from torchvideo.samplers import FullVideoSampler


class TestFullVideoSampler:
    @given(st.integers(min_value=1))
    def test_full_video_sampler(self, length):
        sampler = FullVideoSampler()

        idx_slice = sampler.sample(length)

        assert idx_slice.stop == length
        assert idx_slice.start == 0
        assert idx_slice.step == 1

    def test_full_video_sampler_repr(self):
        assert repr(FullVideoSampler()) == "FullVideoSampler()"

    def test_full_video_sampler_str(self):
        assert str(FullVideoSampler()) == "FullVideoSampler()"
