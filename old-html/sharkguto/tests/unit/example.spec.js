import { shallowMount, createLocalVue } from '@vue/test-utils';
import Vuex from 'vuex';
import HelloWorld from '@/components/HelloWorld.vue';

const localVue = createLocalVue();

localVue.use(Vuex);

describe('HelloWorld.vue', () => {
  let actions;
  let store;

  beforeEach(() => {
    actions = {
      actionClick: jest.fn(),
      actionInput: jest.fn(),
    };
    store = new Vuex.Store({
      actions,
    });
  });


  it('renders props.msg when passed', () => {
    const msg = '';
    const wrapper = shallowMount(HelloWorld, {
      store,
      localVue,
      propsData: { msg },
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
