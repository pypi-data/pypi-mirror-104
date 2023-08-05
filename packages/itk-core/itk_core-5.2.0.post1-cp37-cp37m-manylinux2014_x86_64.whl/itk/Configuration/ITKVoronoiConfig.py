depends = ('ITKPyBase', 'ITKMesh', 'ITKImageFilterBase', )
templates = (
  ('VoronoiSegmentationImageFilter', 'itk::VoronoiSegmentationImageFilter', 'itkVoronoiSegmentationImageFilterIUC2IUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('VoronoiSegmentationImageFilter', 'itk::VoronoiSegmentationImageFilter', 'itkVoronoiSegmentationImageFilterIUS2IUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
)
