import courseManage from '@/components/admin/courseManage'

describe('courseManage', () => {
  it('set a correct data', () => {
    expect(typeof courseManage.data).toBe('function')
    const defaultData = courseManage.data()
    expect(defaultData.courseData[1].courseId).toBe(15223)
    expect(defaultData.courseData[0].courseTitle).toBe('我们爱科学')
  })
})
