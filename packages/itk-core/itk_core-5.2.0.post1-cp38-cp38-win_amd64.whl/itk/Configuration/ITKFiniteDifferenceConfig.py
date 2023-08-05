depends = ('ITKPyBase', 'ITKCommon', )
templates = (
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIF4IF4', True, 'itk::Image< float,4 >, itk::Image< float,4 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterID4ID4', True, 'itk::Image< double,4 >, itk::Image< double,4 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF22IVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF23IVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF24IVF24', True, 'itk::Image< itk::Vector< float,2 >,4 >, itk::Image< itk::Vector< float,2 >,4 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF32IVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF33IVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF34IVF34', True, 'itk::Image< itk::Vector< float,3 >,4 >, itk::Image< itk::Vector< float,3 >,4 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF42IVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF43IVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterIVF44IVF44', True, 'itk::Image< itk::Vector< float,4 >,4 >, itk::Image< itk::Vector< float,4 >,4 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF22ICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF23ICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF24ICVF24', True, 'itk::Image< itk::CovariantVector< float,2 >,4 >, itk::Image< itk::CovariantVector< float,2 >,4 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF32ICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF33ICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF34ICVF34', True, 'itk::Image< itk::CovariantVector< float,3 >,4 >, itk::Image< itk::CovariantVector< float,3 >,4 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF42ICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF43ICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('DenseFiniteDifferenceImageFilter', 'itk::DenseFiniteDifferenceImageFilter', 'itkDenseFiniteDifferenceImageFilterICVF44ICVF44', True, 'itk::Image< itk::CovariantVector< float,4 >,4 >, itk::Image< itk::CovariantVector< float,4 >,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionISS2', True, 'itk::Image< signed short,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionISS3', True, 'itk::Image< signed short,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionISS4', True, 'itk::Image< signed short,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIUC4', True, 'itk::Image< unsigned char,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIUS4', True, 'itk::Image< unsigned short,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIF2', True, 'itk::Image< float,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIF3', True, 'itk::Image< float,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIF4', True, 'itk::Image< float,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionID2', True, 'itk::Image< double,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionID3', True, 'itk::Image< double,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionID4', True, 'itk::Image< double,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF24', True, 'itk::Image< itk::Vector< float,2 >,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF34', True, 'itk::Image< itk::Vector< float,3 >,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionIVF44', True, 'itk::Image< itk::Vector< float,4 >,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF24', True, 'itk::Image< itk::CovariantVector< float,2 >,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF34', True, 'itk::Image< itk::CovariantVector< float,3 >,4 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('FiniteDifferenceFunction', 'itk::FiniteDifferenceFunction', 'itkFiniteDifferenceFunctionICVF44', True, 'itk::Image< itk::CovariantVector< float,4 >,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIF4IF4', True, 'itk::Image< float,4 >, itk::Image< float,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterID4ID4', True, 'itk::Image< double,4 >, itk::Image< double,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF22IVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF23IVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF24IVF24', True, 'itk::Image< itk::Vector< float,2 >,4 >, itk::Image< itk::Vector< float,2 >,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF32IVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF33IVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF34IVF34', True, 'itk::Image< itk::Vector< float,3 >,4 >, itk::Image< itk::Vector< float,3 >,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF42IVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF43IVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterIVF44IVF44', True, 'itk::Image< itk::Vector< float,4 >,4 >, itk::Image< itk::Vector< float,4 >,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF22ICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF23ICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF24ICVF24', True, 'itk::Image< itk::CovariantVector< float,2 >,4 >, itk::Image< itk::CovariantVector< float,2 >,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF32ICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF33ICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF34ICVF34', True, 'itk::Image< itk::CovariantVector< float,3 >,4 >, itk::Image< itk::CovariantVector< float,3 >,4 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF42ICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF43ICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('FiniteDifferenceImageFilter', 'itk::FiniteDifferenceImageFilter', 'itkFiniteDifferenceImageFilterICVF44ICVF44', True, 'itk::Image< itk::CovariantVector< float,4 >,4 >, itk::Image< itk::CovariantVector< float,4 >,4 >'),
)
